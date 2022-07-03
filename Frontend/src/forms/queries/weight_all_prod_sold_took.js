import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import '../form.css';

export default function WeightAllProdSoldTookForm({ flexDirection = "column", ...props }) {
    const [soldierId, setSoldierId] = useState(0);

    props.setParams(() => `soldierId=${soldierId}`);
    return (
        <div>
            <form style={{ display: 'flex', flexDirection: flexDirection }}
                {...props}>
                <div className='form-control'>
                    <TextField
                        name='soldierId'
                        variant="outlined"
                        label="Soldier Id"
                        type="number"
                        value={soldierId}
                        onChange={(ev) => setSoldierId(ev.target.value)}
                        fullWidth
                    />
                </div>
            </form>
        </div>
    );
}