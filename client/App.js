import React, { useEffect } from 'react'
import { BrowserRouter, Switch, Link, Route } from 'react-router-dom'
import './styles/style.scss'
import axios from 'axios'
import MyApp from  "./components/Calendar.js"
import TodoList from './components/todoList'
// ! Some starter code for your frontend, change this
// ! however you like.
const App = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={Home} />
      
    </Switch>
  </BrowserRouter>
)

const Home = () => (
  <div>
  <MyApp />
  <TodoList />
  </div>
)


export default App