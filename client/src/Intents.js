import React, {useState}from 'react';
import { Button, List, ListItem, ListItemText } from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import "./ListComp.css"
import AddIcon from '@mui/icons-material/Add';
import { TextField } from '@mui/material';

const ListComponent = ({ names }) => {
  const [showForm, setShowForm] = useState(false);
  const [intention, setIntention] = useState('');
  const [examples, setExamples] = useState('');
  const [answer, setAnswer] = useState('');
  const handleButtonClick = () => {
    setShowForm(true);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    // Добавьте здесь логику для обработки отправки формы
    console.log('Намерение:', intention);
    console.log('Примеры:', examples);
    // Сбросить значения полей формы
    setIntention('');
    setExamples('');
    // Скрыть форму после отправки
    setShowForm(false);
  };

  return (
    <div class = "ListInt">
      <p>Намерения <Button onClick={ handleButtonClick} variant="contained" color = "secondary"> <AddIcon/></Button></p>
      {showForm && (
        <form onSubmit={handleFormSubmit}>
          <TextField
            label="Намерение"
            value={intention}
            onChange={(e) => setIntention(e.target.value)}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Примеры"
            value={examples}
            onChange={(e) => setExamples(e.target.value)}
            fullWidth
            margin="normal"
          />
          <TextField
            label="Ответ"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            fullWidth
            margin="normal"
          />
          <Button type="submit" variant="contained" color="primary">
            Отправить
          </Button>
        </form>
      )}
    <List>
      {names.map((name, index) => (
        <div class = "list">
        <ListItem key={index}>
          <Button variant="contained">{name}</Button>
          <div class = "buts">
          <Button variant="contained">
           <EditIcon/>
          </Button>
          <div class = 'trash'><Button variant="contained" >
            <DeleteIcon/>
          </Button>
          </div>
          </div>
        </ListItem>
        </div>
      ))}
    </List>

    
      
    </div>
  );
};

export default ListComponent;