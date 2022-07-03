import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import '../form.css';

export default function ProdFromSpeManForm({ flexDirection = 'column', ...props }) {
    const [Id, setId] = useState(0);

    props.setParams(() => `Id=${Id}`);
    return (
        <div style={{width: '250px'}}>
            <form
                style={{ display: 'flex', flexDirection: flexDirection }}
                {...props}
            >
                <div className='form-control'>
                    <TextField
                        name='Id'
                        variant="outlined"
                        label="Manufacturer Id"
                        type="number"
                        value={Id}
                        onChange={(ev) => setId(ev.target.value)}
                        fullWidth
                    />
                </div>
            </form>
        </div>
    );
}