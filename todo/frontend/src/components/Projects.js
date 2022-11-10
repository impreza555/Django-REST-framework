import React from 'react';


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.name}</td>
            <td>{item.link}</td>
            <td>{item.users}</td>
        </tr>
    );
}


const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>Название</th>
                <th>Ссылка</th>
                <th>Пользователи</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    );
}


export default ProjectList;