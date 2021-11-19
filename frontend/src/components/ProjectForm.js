import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../App.css';
import {Redirect} from 'react-router-dom'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }
    handleAuthorsChange(event) {
            if (!event.target.selectedOptions) {
                return;
            }

            let authors = []
            for(let i = 0; i < event.target.selectedOptions.length; i++) {
                authors.push(parseInt(event.target.selectedOptions.item(i).value))
            }

            this.setState({
                ['users']: authors
            })
        }
    handleSubmit(event) {
        console.log(this.state.name, this.state.users)
        this.props.createProject(this.state.name, this.state.users)
        event.preventDefault()

    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="name" placeholder="name" value={this.state.login} onChange = {(event) => this.handleChange(event)} />
                <select multiple name="users" onChange = {(event) => this.handleAuthorsChange(event)}>
                    {this.props.authors.map((author) => <option value={author.id}>{author.firstname} {author.lastname}</option>)}
                </select>
                <input type="submit" value="Создать" />
            </form>
        )
    }
}

export default ProjectForm