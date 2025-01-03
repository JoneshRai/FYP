import * as React from 'react';
import TextField from '@mui/material/TextField';
import { Controller } from 'react-hook-form'; // Corrected the import (capital 'C')

// MyTextField.jsx
export default function MyTextField(props) {
    const { label, name, control } = props;
  
    return (
      <Controller
        name={name}
        control={control}
        render={({ field: { onChange, value }, fieldState: { error } }) => (
          <TextField
            id={`outlined-basic-${name}`}  // Add a unique id for each input
            onChange={onChange}
            value={value || ''}  // Ensure value is always defined
            label={label}
            variant="outlined"
            className={"myform"}
            error={!!error}
            helperText={error?.message}
          />
        )}
      />
    );
  }
  