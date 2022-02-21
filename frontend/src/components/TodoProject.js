import React from 'react'
import { useParams } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

const TodoItem = ({item, deleteToDo}) => {
    let status = ''
    let button;
    if (item.is_active){
        status = 'Активный'
        button = <button onClick={() => deleteToDo(item.id)} type="button" class="btn btn-danger" >Удалить</button>
    }else{
        status = 'Завершен'
        button = <button type="button" class="btn btn-success" >Восстановить</button>
    }


    return (
        <tr>
            <td>{item.text}</td>
            <td>{status}</td>
            <td>{item.create_user.username}</td>
             <td>
               {button}
           </td>
        </tr>
    )
}


const TodoProjectList = ({items, deleteToDo}) => {

    let { id } = useParams();
    let link_add = "/projects/"+String(id)+"/create"
    console.log(link_add, 'linck')
    let filtered_items = items.filter((item) => item.project === Number.parseInt(id))
    console.log(filtered_items)
    return (
        <table class="table">
         <thead>
            <tr >
                <th scope="col">Текст</th>
                <th scope="col">Статус</th>
                <th scope="col">Автор</th>
                <th scope="col"></th>
            </tr>
         </thead>
          <tbody>
            {filtered_items.map((item) => <TodoItem item={item} deleteToDo={deleteToDo} />)}
         </tbody>
         <Link type="button" to={link_add}  class="btn btn-primary" >Добавить</Link>
        </table>

    )
}

export default TodoProjectList