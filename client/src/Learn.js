import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import { ThemeProvider, createTheme } from '@mui/material/styles';
const LearnButton = () => {
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    setIsLoading(true);

    try {
      // Отправка запроса
      const response = await fetch('https://example.com/api');
      const data = await response.json();

      // Обработка ответа

    } catch (error) {
      // Обработка ошибок
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
    <Button onClick={handleClick} disabled={isLoading} variant="contained">
      {isLoading ? <CircularProgress size={20} /> : 'обучить'}
    </Button>
    </ThemeProvider>
  );
};

export default LearnButton;