import React from 'react';
import axios from 'axios';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
//import logo from './logo.svg';
//import './App.css';
import './bootstrap/css/bootstrap.min.css';
import './bootstrap/css/sticky-footer-navbar.css';
import UsersList from './components/Users.js';
import ProjectsList from './components/Projects.js';
import TodoNotesList from './components/TodoNotes.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';


const DOMIAN = 'http://127.0.0.1:8000/api/'
const get_url = (link) => `${DOMIAN}${link}`
const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    );
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            menuItems: [
                {name: 'Пользователи', href: '/'},
                {name: 'Проекты', href: '/projects'},
                {name: 'Заметки', href: '/todo_notes'}
            ],
            'users': [],
            'projects': [],
            'todo_notes': [],
        }
    }

    componentDidMount() {
        axios.get(get_url('users/'))
            .then(response => {
                const users = response.data.results
                    this.setState(
                        {
                            'users': users
                        }
                );
            }).catch(error => console.log(error));

        axios.get(get_url('projects/'))
            .then(response => {
                const projects = response.data.results
                    this.setState(
                        {
                            'projects': projects
                        }
                );
            }).catch(error => console.log(error));

        axios.get(get_url('todo_notes/'))
            .then(response => {
                const todo_notes = response.data.results
                    this.setState(
                        {
                            'todo_notes': todo_notes
                        }
                );
            }).catch(error => console.log(error));
    }

    render () {
        return (
            <div>
                <BrowserRouter>
                    <header>
                        <Menu menuItems={this.state.menuItems} />
                    </header>
                    <main role="main" className="flex-shrink-0">
                        <div className="container">
                            <Routes>
                                <Route exact path='/' element={<UsersList users={this.state.users} />} />
                                <Route exact path='/projects' element={<ProjectsList projects={this.state.projects} />} />
                                <Route exact path='/todo_notes' element={<TodoNotesList todoNotes={this.state.todo_notes} />} />
                                <Route element={NotFound404} />
                            </Routes>
                        </div>
                    </main>
                    <Footer />
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
