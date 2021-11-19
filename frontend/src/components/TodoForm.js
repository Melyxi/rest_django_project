import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';
import {Redirect} from 'react-router-dom'
import {Link} from 'react-router-dom'
import { withRouter } from "react-router";


class TodoForm extends React.Component {
    componentDidMount() {
        const id = this.props.match.params.id;
        this.setState({'id': id})
    }
    constructor(props) {
        super(props)
        this.state = {
            'text': '',
            'id': '',
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }
    handleAuthorsChange(event) {

        }
    handleSubmit(event) {
        console.log(this.state.text, this.state.id)
        this.props.addTodo(this.state.text, this.state.id)
        event.preventDefault()

    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="text" placeholder="Текст" value={this.state.login} onChange = {(event) => this.handleChange(event)} />
                <input type="submit" value="Создать" />
            </form>
        )
    }
}

export default withRouter(TodoForm)