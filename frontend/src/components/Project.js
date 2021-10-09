import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
   return (
       <tr>
           <td>
              <Link to={`projects/${project.id}`}>{project.name}</Link>
           </td>
           <td>
               {project.data_at}
           </td>
       </tr>
   )
}


const ProjectList = ({projects}) => {

   return (
       <table class="table">
       <thead>
          <tr>
           <th scope="col">
               Название проекта
           </th>
           <th scope="col">
               Время создания
           </th>
          </tr>
         </thead>
         <tbody>
            {projects.map((a) => <ProjectItem project={a} />)}
          </tbody>
       </table>
   )
}


export default ProjectList