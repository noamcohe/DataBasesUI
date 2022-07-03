import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import '../form.css';

export default function BuildingsForm(props) {
    const [bName, setBName] = useState('');
    const [position, setPosition] = useState('');
    const [bDescription, setBDescription] = useState('');

    props.setParams(() => `bName=${bName}&position=${position}&bDescription=${bDescription}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <TextField
                        name='bName'
                        variant="outlined"
                        label="Building Name"
                        value={bName}
                        onChange={(ev) => setBName(ev.target.value)}
                        fullWidth
                    />
                </div>

                <div className='form-control'>
                    <TextField
                        name='position'
                        variant="outlined"
                        label="Position"
                        value={position}
                        onChange={(ev) => setPosition(ev.target.value)}
                        fullWidth
                    />
                </div>
                
                <div className='form-control'>
                    <TextField
                        name='bDescription'
                        variant="outlined"
                        label="Building Description"
                        value={bDescription}
                        onChange={(ev) => setBDescription(ev.target.value)}
                        fullWidth
                    />
                </div>
            </form>
        </div>
    );
}