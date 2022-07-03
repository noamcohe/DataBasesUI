import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import AutocompleteComboBox from '../../controls/autocomplete-combo-box';
import '../form.css';

export default function SoldiersForm(props) {
    const [slName, setSlName] = useState('');
    const [sfName, setSfName] = useState('');
    const [Weight, setWeight] = useState();
    const [Rooms, setRooms] = useState('');
    const [Equipment, setEquipment] = useState('');
    const [Duties, setDuties] = useState('');

    props.setParams(() => `slName=${slName}&sfName=${sfName}&Weight=${Weight}&roomId=${Rooms['rid']}&equId=${Equipment['Id']}&dutyId=${Duties['did']}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField
                        name='slName'
                        variant="outlined"
                        label="Last Name"
                        value={slName}
                        onChange={(ev) => setSlName(ev.target.value)}
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='sfName'
                        variant="outlined"
                        label="First Name"
                        value={sfName}
                        onChange={(ev) => setSfName(ev.target.value)}
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
                    <AutocompleteComboBox
                        tableName='Rooms'
                        value={Rooms}
                        columnToShow="rid"
                        handleValueChanged={setRooms}
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Equipment'
                        value={Equipment}
                        columnToShow="Id"
                        handleValueChanged={setEquipment}
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Duties'
                        value={Duties}
                        columnToShow="did"
                        handleValueChanged={setDuties}
                    />
                </div>
            </form>
        </div>
    );
}