import React from 'react';


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    );
}


const ProjectsList = ({projects}) => {
    return (
        <table className="table">
            <th>Название</th>
            <th>Ссылка</th>
            <th>Пользователи</th>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    );
}


export default ProjectsList;