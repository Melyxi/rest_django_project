import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

const ProjectItem = ({project, deleteProject}) => {
   return (
       <tr>
           <td>
              <Link to={`projects/${project.id}`}>{project.name}</Link>
           </td>
           <td>
               {project.data_at}
           </td>
           <td>
                <button onClick={() => deleteProject(project.id)} type="button" class="btn btn-danger" >Удалить</button>
           </td>
       </tr>
   )
}


const ProjectList = ({projects, deleteProject}) => {

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
           <th scope="col">

           </th>
          </tr>
         </thead>
         <tbody>

            {projects.map((a) => <ProjectItem project={a} deleteProject={deleteProject}/>)}
          </tbody>
          <Link class="btn btn-primary" to='projects/create'>Создать</Link>
       </table>


   )
}


export default ProjectList