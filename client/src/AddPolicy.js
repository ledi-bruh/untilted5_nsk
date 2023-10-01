import React from 'react';
import Button from '@mui/material/Button';
import './uploadbuton.css'
import LearnButton from './Learn';
const PolicyButton = () => {
  const handlePolicyUpload = () => {
  };

  return (
    <div class = "download">
      <p>Загрузите новые данные для обучения бота</p>
    <div  class = "buttons">
    <Button
  variant="contained"
  component="label"
>
  Upload File
  <input
    type="file"
    hidden
  />
  </Button>
    <div class = "Learnbutton"><LearnButton /></div>
  </div>
  </div>
  );
};

export default PolicyButton;