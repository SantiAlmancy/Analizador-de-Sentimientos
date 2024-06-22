import './Table.css';
import DataTable from 'react-data-table-component'

const Table = (props) => {
    return (
        <div className="dataTable">
            <DataTable 
                columns={props.columns} 
                data={props.data} 
                pagination
                fixedHeader
                fixedHeaderScrollHeight={props.height}
                highlightOnHover
            />
        </div>
    );
}

export default Table;
