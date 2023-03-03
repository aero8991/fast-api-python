export default function Search(props) {

  return (


    <div>
      <input onChange={props.change} placeholder="Search..." className="Search-box"></input>
    </div>
  );
}
