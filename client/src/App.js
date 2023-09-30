
import './App.css';
import React , { useState }  from "react";
import { AppBar, Button, Toolbar, Typography, IconButton, Menu, MenuItem } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import PolicyButton from './AddPolicy';
import ListComponent from './Intents';
import { ThemeProvider, createTheme } from '@mui/material/styles';

function App() {
 
      const [anchorEl, setAnchorEl] = React.useState(null);
      const [showComponent, setShowComponent] = useState(false);
      const [showComponent2, setShowComponent2] = useState(false);
      const handleMenuClick = (event) => {
        setAnchorEl(event.currentTarget);
      };
    

     const  handleAddIntent =() =>{
      setShowComponent2(true);
      setShowComponent(false);
        setAnchorEl(null);
        
      }
      const handleMenuClose = () => {
        setAnchorEl(null);
      };

      const handleAddpolicy =() =>{
        setAnchorEl(null);
        setShowComponent(true);
        setShowComponent2(false);
      }
    

      const darkTheme = createTheme({
        palette: {
          mode: 'dark',
          primary: {
            main: '#1976d2',
          },
        },
      });

      
      return (
        <div>
           <ThemeProvider theme={darkTheme}>
        <AppBar position="static" sx={{ flexGrow: 1 }}>
          <Toolbar >
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              onClick={handleMenuClick}
            >
              <MenuIcon />
            </IconButton>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Меню
            </Typography>
            <Menu
              anchorEl={anchorEl}
              open={Boolean(anchorEl)}
              onClose={handleMenuClose}
            >
              <MenuItem onClick={handleAddIntent}>Намерения
              </MenuItem>
              <MenuItem onClick={handleAddpolicy}>Добавить политику</MenuItem>
              
            </Menu>
            <Button color="inherit">Вход</Button>
          </Toolbar>
        </AppBar>
         {showComponent &&  <div class = "button"><PolicyButton /></div>}
         {showComponent2 &&  <ListComponent names =  {['Приветсви1', 'Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1','Приветсви1']}/>}
         </ThemeProvider>
         </div>
        
      );
    
   
    
}

export default App;
