import React from 'react';
import {Link, useParams} from "react-router-dom";


const ProjectItem = ({project}) => {
    let link_detail = `/projects/${project.id}`
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.link}</td>
            <td><Link to={link_detail}>{project.id}</Link></td>
        </tr>
    );
}


const ProjectsList = ({projects}) => {
    return (
        <table className="table">
            <tr>
                <th>Название</th>
                <th>Ссылка</th>
                <th>Подробности</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project}/>)}
        </table>
    );
}


const ProjectDetailItem = ({project}) => {
    return (
        <li>
            {project.user.username}
        </li>
    )
}


const ProjectDetail = ({projects}) => {
    let {id} = useParams();
    let filtered_projects = projects.filter((projects) => projects.users.id == id)
    return (
        <table className="table">
            <tr>
                <td>{projects.name}</td>
                <td>{projects.link}</td>
                <td>Пользователи</td>
            </tr>
            <ul>
                {filtered_projects.map((project) => <ProjectDetailItem project={project}/>)}
            </ul>
        </table>
    )
}


export {ProjectsList, ProjectDetail};