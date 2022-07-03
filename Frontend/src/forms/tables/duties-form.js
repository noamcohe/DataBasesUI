import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import '../form.css';

export default function DutiesForm(props) {
    const [did, setDid] = useState();
    const [dName, setDName] = useState('');
    const [dDescription, setDDescription] = useState('');
    props.setParams(()=>`did=${did}&dName=${dName}&dDescription=${dDescription}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField 
                        name='did'
                        variant="outlined" 
                        label="Duty Id"
                        type="number"
                        value={did}
                        onChange={(ev)=>setDid(ev.target.value)}
                        />
                </div>

                <div className='form-control'>
                    <TextField
                        name='dName'
                        variant="outlined"
                        label="Duty Name"
                        value={dName}
                        onChange={(ev)=>setDName(ev.target.value)}
                        />
                </div>

                <div className='form-control'>
                    <TextField
                        name='dDescription'
                        variant="outlined"
                        label="Duty Description"
                        value={dDescription}
                        onChange={(ev)=>setDDescription(ev.target.value)}
                        />
                </div>
            </form>
        </div>
    );
}