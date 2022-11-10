import React from 'react';
import axios from 'axios';
//import logo from './logo.svg';
//import './App.css';
import './bootstrap/css/bootstrap.min.css';
import './bootstrap/css/sticky-footer-navbar.css';
import UserList from './components/User.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';


const DOMIAN = 'http://127.0.0.1:8000/api/'
const get_url = (link) => `${DOMIAN}${link}`


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            menuItems: [
                {name: 'Пользователи', href: '/'},
            ],
            'users': []
        }
    }

    componentDidMount() {
        axios.get(get_url('users'))
            .then(response => {
                const users = response.data.results
                    this.setState(
                        {
                            'users': users
                        }
                );
            }).catch(error => console.log(error));
    }

    render () {
        return (
            <div>
                <header>
                    <Menu menuItems={this.state.menuItems} />
                </header>
                <main role="main" class="flex-shrink-0">
                    <div className="container">
                        <UserList users={this.state.users} />
                    </div>
                </main>
                <Footer />
            </div>
        );
    }
}

export default App;
