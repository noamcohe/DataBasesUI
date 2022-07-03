import React from 'react';
import ManufacturerForm from './tables/manufacturer-form';
import DutiesForm from './tables/duties-form';
import LendingForm from './tables/lending-form';
import SoldiersForm from './tables/soldiers-form';
import RoomsForm from './tables/rooms-form';
import BuildingsForm from './tables/buildings-form';
import EquipmentForm from './tables/equipment-form';
import VehiclesForm from './tables/vehicles-form';

/**
 *
 * @param {String} param0
 */
export default function FormSelector({ tableName='', setParams }) {
    tableName = tableName.toLowerCase();
    const forms = {
        Duties: <DutiesForm setParams={setParams} />,
        Manufacturer: <ManufacturerForm setParams={setParams} />,
        Lending: <LendingForm setParams={setParams} />,
        Soldiers: <SoldiersForm setParams={setParams} />,
        Rooms: <RoomsForm setParams={setParams} />,
        Buildings: <BuildingsForm setParams={setParams} />,
        Equipment: <EquipmentForm setParams={setParams} />,
        Vehicles: <VehiclesForm setParams={setParams} />,
    };

    return tableName in forms ? forms[tableName] : 'Error';
}