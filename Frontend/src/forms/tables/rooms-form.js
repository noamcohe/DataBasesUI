import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import AutocompleteComboBox from '../../controls/autocomplete-combo-box';
import '../form.css';

export default function RoomsForm(props) {
    const [rid, setRid] = useState();
    const [rNumber, setRNumber] = useState(-1);
    const [Buildings, setBuildings] = useState('');
    const [size, setSize] = useState(-1);
    const [rDescription, setRDescription] = useState('');
    const [numOfSoldiers, setNumOfSoldiers] = useState();
    const [maxSoldiers, setMaxSoldiers] = useState();

    props.setParams(() => `rid=${rid}&rNumber=${rNumber}&buildingId=${Buildings['bid']}&size=${size}&rDescription=${rDescription}&numOfSoldiers=${numOfSoldiers}&maxSoldiers=${maxSoldiers}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField
                        name='rid'
                        variant="outlined"
                        label="Room Id"
                        type="number"
                        value={rid}
                        onChange={(ev) => setRid(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='rNumber'
                        variant="outlined"
                        label="Room Number"
                        type="number"
                        value={rNumber}
                        onChange={(ev) => setRNumber(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Buildings'
                        value={Buildings}
                        columnToShow="bid"
                        handleValueChanged={setBuildings}
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='size'
                        variant="outlined"
                        label="size"
                        type="number"
                        value={size}
                        onChange={(ev) => setSize(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='rDescription'
                        variant="outlined"
                        label="Room Description"
                        value={rDescription}
                        onChange={(ev) => setRDescription(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='numOfSoldiers'
                        variant="outlined"
                        label="Num Of Soldiers"
                        type="number"
                        value={numOfSoldiers}
                        onChange={(ev) => setNumOfSoldiers(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='maxSoldiers'
                        variant="outlined"
                        label="Max Of Soldiers"
                        type="number"
                        value={maxSoldiers}
                        onChange={(ev) => setMaxSoldiers(ev.target.value)}
                        fullWidth
                    />
                </div>
            </form>
        </div>
    );
}