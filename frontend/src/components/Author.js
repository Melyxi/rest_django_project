import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';

const AuthorItem = ({author}) => {
   return (
       <tr>
           <td>
               {author.firstname}
           </td>
           <td>
               {author.lastname}
           </td>
           <td>
               {author.email}
           </td>

       </tr>
   )
}


const AuthorList = ({authors}) => {
   return (
       <table class="table">
       <thead>
          <tr>
           <th scope="col">
               Имя
           </th>
           <th scope="col">
               Фамилия
           </th>
           <th scope="col">
               email
           </th>
          </tr>
         </thead>
         <tbody>
            {authors.map((a) => <AuthorItem author={a} />)}
          </tbody>
       </table>
   )
}


export default AuthorList