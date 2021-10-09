import React from 'react';
import './App.css';
import axios from 'axios'
import AuthorList from './components/Author.js'
import FooterIndex from './components/Footer.js'
import MenuIndex from './components/Menu.js'
import {HashRouter, Route, Switch} from 'react-router-dom'
import ProjectList from './components/Project.js'
import TodoProjectList from './components/TodoProject.js'


const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}



class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'projects': [],
           'todo': []
       }
    }

   componentDidMount(){
       axios.get('http://127.0.0.1:8000/api/authors/')
           .then(response => {
               const authors = response.data
                   this.setState(
                   {
                       'authors': authors.results
                   }
               )
           }).catch(error => console.log(error))


       axios.get('http://127.0.0.1:8000/api/project/')
           .then(response => {
               const project = response.data
                   console.log(project.results)
                   this.setState(
                   {
                       'projects': project.results
                   }
               )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/todo/')
           .then(response => {
               const todo = response.data

                   this.setState(
                   {
                       'todo': todo.results
                   }
               )
           }).catch(error => console.log(error))

    }


   render () {
       return (

           <div>
           <HashRouter>

                <MenuIndex />
                <Switch>
                        <Route exact path='/authors' component={() =>  <AuthorList authors={this.state.authors} />}  />
                        <Route exact path='/projects' component={() =>  <ProjectList projects={this.state.projects} />}  />
                        <Route path="/projects/:id"><TodoProjectList items={this.state.todo} /></Route>

                         <Route component={NotFound404} />
                         </Switch>
           </HashRouter>
                 <FooterIndex />
           </div>



       );
   }
}

export default App;