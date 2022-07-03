import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import '../form.css';

export default function ManufacturerForm(props) {
    const [Name, setName] = useState('');
    props.setParams(()=>`name=${name}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField 
                        name='Name'
                        variant="outlined" 
                        label="Manufacturer Name"
                        value={Name}
                        onChange={(ev)=>setName(ev.target.value)} 
                        fullWidth
                        />
                </div>
            </form>
        </div>
    );
}