import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import AutocompleteComboBox from '../../controls/autocomplete-combo-box';
import '../form.css';

export default function VehiclesForm(props) {
    const [vid, setVid] = useState();
    const [vType, setVType] = useState('');
    const [vModel, setVModel] = useState('');
    const [Buildings, setBuildings] = useState('');
    const [vDescription, setVDescription] = useState('');
    const [maxWight, setMaxWight] = useState();

    props.setParams(() => `vid=${vid}&vType=${vType}&vModel=${vModel}&buildingId=${Buildings['bid']}&vDescription=${vDescription}&maxWight=${maxWight}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField
                        name='vid'
                        variant="outlined"
                        label="Vehicle Id"
                        type="number"
                        value={vid}
                        onChange={(ev) => setVid(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='vType'
                        variant="outlined"
                        label="Vehicle Type"
                        value={vType}
                        onChange={(ev) => setVType(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='vModel'
                        variant="outlined"
                        label="Vehicle Model"
                        value={vModel}
                        onChange={(ev) => setVModel(ev.target.value)}
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
                        name='vDescription'
                        variant="outlined"
                        label="Vehicle Description"
                        value={vDescription}
                        onChange={(ev) => setVDescription(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='maxWight'
                        variant="outlined"
                        label="maxWight"
                        type="number"
                        value={maxWight}
                        onChange={(ev) => setMaxWight(ev.target.value)}
                        fullWidth
                    />
                </div>
            </form>
        </div>
    );
}