import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def group_adjust(vals, groups, weights):
    """
    Calculate a group adjustment (demean).

    Parameters
    ----------

    vals    : List of floats/ints

        The original values to adjust

    groups  : List of Lists

        A list of groups. Each group will be a list of ints

    weights : List of floats

        A list of weights for the groupings.

    Returns
    -------

    A list-like demeaned version of the input values
    """
    # data frame for all series
    dataSize = len(vals)

    if len(groups) != len(weights):
        raise ValueError('group and weight count mismatch')

    countries = groups[0]

    if len(countries) != dataSize:
        raise ValueError('Country group size mismatch with values')
        return False


    '''
    Countries Size adjustment per Data size 
    if countries and len(countries) < dataSize:
        countries = countries[:1] * dataSize
    elif len(countries) > dataSize:
        countries = countries[:dataSize]
    '''

    states = groups[1]
    if len(states) != dataSize:
        raise ValueError('State group size mismatch with values')
        return False

    '''
    State Size adjustment per Data size 
    if states and len(states) < dataSize:
        states = states[:1] * dataSize
    elif len(states) > dataSize:
        states = states[:dataSize]
    '''
    city_mean = None

    # combined data frame to do stat. operation
    if len(groups) == 3:
        cities = groups[2]
        combined = pd.DataFrame(
            dict(
                Countries=countries,
                States=states,
                Cities=cities,
                values=vals,
            )
        )
        city_mean = combined.groupby(['Countries', 'States', 'Cities']).transform('mean')
    else:
        combined = pd.DataFrame(
            dict(
                Countries=countries,
                States=states,
                values=vals,
            )
        )
    # transform mean to all rows
    logging.info('input set:\n{0}'.format(combined))
    country_mean = combined.groupby('Countries').transform('mean')
    state_mean = combined.groupby(['Countries', 'States']).transform('mean')


    logging.debug('Country mean:\n{0}'.format(country_mean))

    # weighted mean dataframe set
    wt_country_mean = country_mean * weights[0]
    wt_state_mean = state_mean * weights[1]

    if len(groups) == 3:
        wt_city_mean = city_mean * weights[2]
        result = pd.concat([
            wt_country_mean,
            wt_state_mean,
            wt_city_mean
        ], keys=['Country_mean', 'State_mean', 'City_mean'], axis=1)
    else:
        result = pd.concat([
            wt_country_mean,
            wt_state_mean
        ], keys=['Country_mean', 'State_mean'], axis=1)

    logging.info('weighted mean set:\n{0}'.format(result))

    # row wise sum
    sum_array = result.sum(axis=1).values
    logging.debug('row sum:\n{0}'.format(sum_array))

    # rows index numpy array
    idx = result.index.values + 1

    # index+1 - sum
    res = idx - sum_array
    logging.debug('results:\n{0}'.format(res))

    # updating result set with NaN
    nanIdx = combined[combined['values'].isnull()].index.values
    for idx in nanIdx:
        res[idx] = np.nan

    logging.debug('results after NaN process:\n{0}'.format(res))
    return res



if __name__ == '__main__':
    # vals = [1, 2, 3, 8, 5]
    # grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    # grps_2 = ['MA', 'MA', 'MA', 'RI', 'RI']
    # grps_3 = ['WEYMOUTH', 'BOSTON', 'BOSTON', 'PROVIDENCE', 'PROVIDENCE']
    # weights = [.15, .35, .5]
    #
    # adj_vals = group_adjust(vals, [grps_1, grps_2, grps_3], weights)

    # vals = [1, 2, 3, 8, 5]
    # grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    # grps_2 = ['MA', 'RI', 'CT', 'CT', 'CT']
    # weights = [.65, .35]
    #
    # adj_vals = group_adjust(vals, [grps_1, grps_2], weights)

    # vals = [1, np.NaN, 3, 5, 8, 7]
    # # vals = [1, None, 3, 5, 8, 7]
    # grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA', 'USA']
    # grps_2 = ['MA', 'RI', 'RI', 'CT', 'CT', 'CT']
    # weights = [.65, .35]

    vals = [1, 2, 3, 8, 5]
    grps_1 = ['USA', 'USA', 'USA', 'USA', 'USA']
    grps_2 = ['MA', 'MA', 'MA', 'RI', 'RI']
    grps_3 = ['WEYMOUTH', 'BOSTON', 'BOSTON', 'PROVIDENCE', 'PROVIDENCE']
    weights = [.15, .35, .5]


    group_adjust(vals, [grps_1, grps_2, grps_3], weights)
    #

    #adj_vals = group_adjust(vals, [grps_1, grps_2], weights)
    #