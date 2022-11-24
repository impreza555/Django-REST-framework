import React from 'react';


const TodoNoteItem = ({todoNote}) => {
    return (
        <tr>
            <td>{todoNote.project}</td>
            <td>{todoNote.text}</td>
            <td>{todoNote.creaton_date}</td>
            <td>{todoNote.modifided_date}</td>
            <td>{todoNote.user}</td>
        </tr>
    );
}


const TodoNotesList = ({todoNotes}) => {
    return (
        <table className="table">
            <th>Проект</th>
            <th>Текст</th>
            <th>Дата создания</th>
            <th>Дата изменения</th>
            <th>Пользователь</th>
            {todoNotes.map((todoNote) => <TodoNoteItem todoNote={todoNote}/>)}
        </table>
    );
}


export default TodoNotesList;