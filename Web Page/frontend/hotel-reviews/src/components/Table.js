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
                fixedHeaderScrollHeight='475px'
                highlightOnHover
            />
        </div>
    );
}

export default Table;
