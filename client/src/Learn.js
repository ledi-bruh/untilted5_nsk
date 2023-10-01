import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import { ThemeProvider, createTheme } from '@mui/material/styles';
const LearnButton = () => {
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async (event) => {
    setIsLoading(true);
    const file = event.target.files[0];

    const formData = new FormData();
    formData.append('file', file);

    
    try {
      const response = await fetch('localhost:12222/md', {
        method: 'PUT',
        body: formData
      });
      console.log(response);
      
    } catch (error) {
      console.error(error);
      
    }

    setIsLoading(false);
  };
  const darkTheme = createTheme({
    palette: {
      mode: 'dark',
      primary: {
        main: '#1976d2',
      },
    },
  });


  return (
    <ThemeProvider theme={darkTheme}>
      <input type="file" onChange={handleClick} />
    <Button onClick={handleClick} disabled={isLoading} variant="contained">
      {isLoading ? <CircularProgress size={20} /> : 'обучить'}
    </Button>
    </ThemeProvider>
  );
};

export default LearnButton;