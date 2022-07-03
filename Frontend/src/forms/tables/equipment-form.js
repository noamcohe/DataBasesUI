import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import Checkbox from '@material-ui/core/Checkbox';
import { FormControlLabel } from '@material-ui/core';
import '../form.css';
import AutocompleteComboBox from '../../controls/autocomplete-combo-box';

export default function EquipmentForm(props) {
    const [Name, setName] = useState('');
    const [MinOfStack, setMinOfStack] = useState(10);
    const [Amount, setAmount] = useState(0);
    const [Weight, setWeight] = useState(0);
    const [worker, setWorker] = useState(true);
    const [Rooms, setRooms] = useState('');
    const [eDescription, setEDescription] = useState('');
    const [cost, setCost] = useState();
    const [Vehicles, setVehicles] = useState('');
    const [area, setArea] = useState();
    const [Manufacturer, setManufacturer] = useState('');

    props.setParams(() => `Name=${Name}&MinOfStack=${MinOfStack}&ManufacturerId=${Manufacturer['Id']}&Amount=${Amount}&Weight=${Weight}&worker=${worker}&roomId=${Rooms['rid']}&eDescription=${eDescription}&cost=${cost}&onVehicleId=${Vehicles}&area=${area}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField
                        name='Name'
                        variant="outlined"
                        label="Name"
                        value={Name}
                        onChange={(ev) => setName(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='MinOfStack'
                        variant="outlined"
                        label="Min Of Stack"
                        type="number"
                        value={MinOfStack}
                        onChange={(ev) => setMinOfStack(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Manufacturer'
                        value={Manufacturer}
                        label='Manufacturer'
                        columnToShow="Name"
                        handleValueChanged={setManufacturer}
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='Amount'
                        variant="outlined"
                        label="Amount"
                        type="number"
                        value={Amount}
                        onChange={(ev) => setAmount(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='Weight'
                        variant="outlined"
                        label="Weight"
                        type="number"
                        value={Weight}
                        onChange={(ev) => setWeight(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <FormControlLabel
                        control={<Checkbox
                            color="primary"
                            inputProps={{ 'aria-label': 'secondary checkbox' }}
                            checked={worker}
                            onChange={(ev) => setWorker(ev.target.checked)}
                        />}
                        label='Is work'
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Rooms'
                        value={Rooms}
                        label='Rooms'
                        columnToShow="rNumber"
                        handleValueChanged={setRooms}
                    />
                </div>
                
                <div className='form-control'>
                    <TextField
                        name='eDescription'
                        variant="outlined"
                        label="Description"
                        value={eDescription}
                        onChange={(ev) => setEDescription(ev.target.value)}
                    />
                </div>
                
                <div className='form-control'>
                    <TextField
                        name='cost'
                        variant="outlined"
                        label="cost"
                        type="number"
                        value={cost}
                        onChange={(ev) => setCost(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Vehicles'
                        value={Vehicles}
                        label='Vehicles'
                        columnToShow="vid"
                        handleValueChanged={setVehicles}
                    />
                </div>
                
                <div className='form-control'>
                    <TextField
                        name='area'
                        variant="outlined"
                        label="area"
                        type="number"
                        value={area}
                        onChange={(ev) => setArea(ev.target.value)}
                    />
                </div>
            </form>
        </div>
    );
}