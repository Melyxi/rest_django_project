import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';


class RegistrationForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'username': '',
            'email': '',
            'password': '',
            'password2': ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleSubmit(event) {

        this.props.getToken(this.state.username, this.state.password, this.state.password2, this.state.email)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="username" placeholder="username" value={this.state.username} onChange = {(event) => this.handleChange(event)} />
                <input type="text" name="email" placeholder="email" value={this.state.email} onChange = {(event) => this.handleChange(event)} />
                <input type="password" name="password" placeholder="password" value={this.state.password} onChange = {(event) => this.handleChange(event)} />
                <input type="password" name="password2" placeholder="password2" value={this.state.password2} onChange = {(event) => this.handleChange(event)} />
                <input type="submit" value="Sign-up" />
            </form>
        )
    }
}

export default RegistrationForm