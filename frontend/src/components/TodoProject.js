import React from 'react'
import { useParams } from 'react-router-dom'

const TodoItem = ({item}) => {
    let status = ''
    if (item.is_active){
        status = 'Активный'
    }else{
        status = 'Завершен'
    }
    return (
        <tr>
            <td>{item.text}</td>
            <td>{status}</td>
            <td>{item.create_user.username}</td>
        </tr>
    )
}


const TodoProjectList = ({items}) => {

    let { id } = useParams();
    console.log(items)
    let filtered_items = items.filter((item) => item.project === Number.parseInt(id))
    console.log(filtered_items)
    return (
        <table>
            <tr>
                <th>Текст</th>
                <th>Статус</th>
                <th>Автор</th>
            </tr>
            {filtered_items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default TodoProjectList