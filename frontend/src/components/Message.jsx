



import React from 'react';
import { Box } from '@mui/material'; 

const MyMessage = ({ text }) => {
    return (
        <Box sx={{ backgroundColor: '#69C9AB', color: '#FFFFFF', width: '90%', height: '40px'}}>
            {text}
        </Box>
    );
}

export default MyMessage;
