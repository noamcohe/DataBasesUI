import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import AutocompleteComboBox from '../../controls/autocomplete-combo-box';
import { KeyboardDatePicker, MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import {dateNumberToString} from '../../utils';
import '../form.css';

export default function LendingForm(props) {
    const [Soldiers, setSoldiers] = useState('');
    const [Equipment, setEquipment] = useState('');
    const [DateOfLending, setDateOfLending] = useState(Date.now());
    const [DateOfReturn, setDateOfReturn] = useState();

    props.setParams(() => `SoldierId=${Soldiers['soldierId']}&EquipmentId=${Equipment['Id']}&DateOfLending=${dateNumberToString(DateOfLending)}&EquipmentWeight=${Equipment['Weight']}&DateOfReturn=${dateNumberToString(DateOfReturn)}`);
    return (
        <div>
            <form {...props}>
                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Soldiers'
                        value={Soldiers}
                        columnToShow='soldierId'
                        handleValueChanged={setSoldiers}
                    />
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Equipment'
                        value={Equipment}
                        columnToShow='Id'
                        handleValueChanged={setEquipment}
                    />
                </div>

                <div className='form-control'>
                    <MuiPickersUtilsProvider utils={DateFnsUtils}>
                        <KeyboardDatePicker
                            disableToolbar
                            variant="inline"
                            inputVariant="outlined"
                            format="dd/MM/yyyy"
                            margin="normal"
                            label="Date Of Lending"
                            value={DateOfLending}
                            onChange={setDateOfLending}
                            KeyboardButtonProps={{
                                'aria-label': 'change date',
                            }}
                            fullWidth
                        />
                    </MuiPickersUtilsProvider>
                </div>

                <div className='form-control'>
                    <AutocompleteComboBox
                        tableName='Equipment'
                        value={Equipment}
                        columnToShow='Weight'
                        handleValueChanged={setEquipment}
                    />
                </div>

                <div className='form-control'>
                    <MuiPickersUtilsProvider utils={DateFnsUtils}>
                        <KeyboardDatePicker
                            disableToolbar
                            variant="inline"
                            inputVariant="outlined"
                            format="dd/MM/yyyy"
                            margin="normal"
                            label="Date Of Return"
                            value={DateOfReturn}
                            onChange={setDateOfReturn}
                            KeyboardButtonProps={{
                                'aria-label': 'change date',
                            }}
                            fullWidth
                        />
                    </MuiPickersUtilsProvider>
                </div>
            </form>
        </div>
    );
}