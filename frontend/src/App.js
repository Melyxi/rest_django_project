import React from 'react';
import './App.css';
import axios from 'axios'
import AuthorList from './components/Author.js'
import FooterIndex from './components/Footer.js'
import {HashRouter, Route, Switch} from 'react-router-dom'
import ProjectList from './components/Project.js'
import TodoProjectList from './components/TodoProject.js'
import LoginForm from './components/LoginForm.js'
import ProjectForm from './components/ProjectForm.js'
import {Link} from 'react-router-dom'
import TodoForm from './components/TodoForm.js'
import { useParams } from 'react-router-dom'
import RegistrationForm from './components/RegForm.js'

const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}
const main = () => {
  return (
    <div>
        <h1>Главная</h1>
    </div>
  )
}


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'projects': [],
           'todo': [],
            'token': '',
            'id': ''
       }

    }
    getToken(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
        .then(response => {
            console.log(response.data.token)
            localStorage.setItem('token', response.data.token)
            this.setState({'token': response.data.token}, this.loadData)

        })
        .catch(error => alert("Wrong password"))
    }

        logout() {
        localStorage.setItem('token', '')
        this.setState({'token': ''}, this.loadData)

        }

    isAuthenticated() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuthenticated()) {
            return {'Authorization': 'JWT ' + this.state.token}
        }
        return {}
    }



    loadData() {
        const headers = this.getHeaders()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
           .then(response => {
               const authors = response.data
                   this.setState(
                   {
                       'authors': authors.results
                   }
               )
        })
        .catch(error => {
            console.log(error)
            this.setState({
                'authors': []
            })
        })


       axios.get('http://127.0.0.1:8000/api/project/', {headers})
       .then(response => {
               const project = response.data
                   console.log(project.results)
                   this.setState(
                   {
                       'projects': project.results
                   }
               )
        })
        .catch(error => {
            console.log(error)
            this.setState({
                'projects': []
            })
        })
        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
        .then(response => {
               const todo = response.data

                   this.setState(
                   {
                       'todo': todo.results
                   }
               )
           }).catch(error => {
            console.log(error)
            this.setState({
                'todo': []
            })
        })
    }
    deleteProject(id) {

        console.log(id)
        const headers = this.getHeaders()
        axios.delete(`http://127.0.0.1:8000/api/project/${id}`, {headers})
            .then(response => {
              this.setState({projects: this.state.projects.filter((item)=>item.id !== id)})
            }).catch(error => {console.log(error)})
        }
    deleteToDo(id) {

        console.log(id)
        const headers = this.getHeaders()
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
            .then(response => {
             this.setState(this.loadData)
            }).catch(error => {console.log(error)})
        }
    createProject(name, authors) {

        console.log(name, authors)
        const headers = this.getHeaders()
        axios.post('http://127.0.0.1:8000/api/project/', {'name': name, 'users': authors} , {headers})
        .then(response => {
            console.log("123")
            this.loadData();
        })
        .catch(error => {
            console.log("error")

            console.log(error)
        })
    }

    addTodo(text, id){

        const headers = this.getHeaders()

        axios.post(`http://127.0.0.1:8000/api/projects/${id}/create/`, {'text': text} , {headers})
        .then(response => {
            console.log("123")
            this.loadData();
        })
        .catch(error => {
            console.log("error")

            console.log(error)
        })
    }

    AddUser(username, password, password2, email){
        const headers = this.getHeaders()

        axios.post(`http://127.0.0.1:8000/api/registration/`, {'username': username, 'password': password, 'password2': password2, 'email': email} , {headers})
        .then(response => {

            this.loadData();
        })
        .catch(error => {
            console.log("error")

            console.log(error)
        })


    }

   componentDidMount(){

        const token = localStorage.getItem('token')
        console.log(token)
        this.setState({'token': token}, this.loadData)
    }




   render () {
       return (

           <div>
           <HashRouter>

                    <div class="p-3 bg-dark text-white">
                            <div class="container">
                              <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
                                <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
                                  <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"></svg>
                                </a>

                                <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                                  <li><a href="#" class="nav-link px-2 text-secondary">Home</a></li>
                                    <Link class="nav-link px-2 text-white" to='/authors'>Пользователи</Link>
                                    <Link class="nav-link px-2 text-white" to='/projects'>Проекты</Link>


                                </ul>

                                <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3">
                                  <input type="search" class="form-control form-control-dark" placeholder="Search..." aria-label="Search"/>
                                </form>

                                <div class="text-end">
                                               { this.isAuthenticated() ?
                                                    <button class="btn btn-outline-light me-2" onClick={()=>this.logout()}>Logout</button> :
                                                    <Link class="btn btn-outline-light me-2" to='/login'>Login</Link>
                                                }


                                </div>
                                <Link class="btn btn-warning" to='/registration'>Sign-up</Link>
                              </div>
                            </div>
                          </div>
                <Switch>

                        <Route path='/authors' exact component={() =>  <AuthorList authors={this.state.authors} />}  />
                        <Route path='/' exact component={main}  />
                        <Route path='/projects' exact component={() =>  <ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/>}  />
                        <Route path='/projects/create' exact component={() => <ProjectForm authors = {this.state.authors} createProject={(name, authors) => this.createProject(name, authors)}/>} />
                        <Route path='/projects/:id/create' exact component={() => <TodoForm authors = {this.state.authors} addTodo={(text, id) => this.addTodo(text, id)}/>} />
                        <Route path="/projects/:id"><TodoProjectList items={this.state.todo} deleteToDo={(id)=>this.deleteToDo(id)}/>} /></Route>
                        <Route path='/login' exact component={() => <LoginForm getToken={(login, password) => this.getToken(login, password)} />} />
                        <Route path='/registration' exact component={() => <RegistrationForm AddUser={(username, password, password2, email) => this.AddUser(username, password, password2, email)} />} />

                         <Route component={NotFound404} />
                </Switch>
           </HashRouter>
                 <FooterIndex />
           </div>



       );
   }
}

export default App;