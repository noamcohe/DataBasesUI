import React from 'react';
import AllProductsThatSoldierTookForm from './all_products_that_soldier_took';
import ProdFromSpeManForm from './prod_from_spe_man';
import WeightAllProdSoldTookForm from './weight_all_prod_sold_took';

/**
 *
 * @param {String} param0
 */
export default function QueriesSelector({ queryName='', setParams }) {
    queryName = queryName.toLowerCase();
    const queryForms = {
        all_products_that_soldier_took: <AllProductsThatSoldierTookForm setParams={setParams} flexDirection='row' />,
        prod_from_spe_man: <ProdFromSpeManForm setParams={setParams}  flexDirection='row' />,
        weight_all_prod_sold_took: <WeightAllProdSoldTookForm setParams={setParams} flexDirection='row' />,
    };

    return queryName in queryForms ? queryForms[queryName] : 'Error';
}