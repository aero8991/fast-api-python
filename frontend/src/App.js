import { getPosts, getLine, getData, fastapi } from "./api/axios";
import { useEffect, useState } from "react";
import axios from "axios";

import "./App.css";
import Search from "./components/Search";
import Table from "./components/Table";
import SearchBar from "./components/SearchBar";
import ListPage from "./components/ListPage";
import Connection from "./examples/Connection";

function App() {
  //database

  const [message, setMessage] = useState([]);
  const [searchData, setSearchData] = useState(null);
  const [params, setParams] = useState("");
  const [search, setSearch] = useState("new")

  /// test api
  const [posts, setPosts] = useState([]);
  const [searchResults, setSearchResults] = useState([]);

  const getWelcomeMessage = async () => {
    const reqeustOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "GET",
      },
    };
    // const parameters ={query: setParams(()=> params)}}

    const response = await fetch(
      `/search?query=${encodeURIComponent(params)}`,
      reqeustOptions
    );
    const data = await response.json();
    setSearchData(data.data.splice(0, 10));

    if (!response.ok) {
      console.log("Something is broken...");
    } else {
      setMessage(() => data.data);
    }
  };

  function ChangeHandler() {
    console.log(params);
    setParams(() => params);
  }

  const handleUpdate = async () => {
    try {
      const reponseSearch = await fastapi.get(
        `http://127.0.0.1:8000/search/?query=${search}`
      );
      // const results = await reponseSearch.json();
      //   // const data = await reponseSearch.json();
      //   // setSearchData(reponseSearch.data);
      setSearchData(() => reponseSearch.data);

      console.log(searchData);
    } catch (err) {
      console.log(`Error: ${err}`);
    }
  }

 
  useEffect(() => {
     handleUpdate()
  }, [search]);

  if (!searchData){
    return <h1>waiting for data to load</h1>
  } else{

  return (
    <div className="App">
      <h1>Hello World!</h1>
      <SearchBar
        posts={posts}
        setSearchResults={setSearchResults}
        setSearch={setSearch} />
      
      {/* <ListPage searchResults={searchResults} /> */}
      {/* <Search change={ChangeHandler} /> */}
      {/* <Table data={searchData} />  */}
      <Table data={searchData} />

      {/* <button onClick={getWelcomeMessage}> Select</button> */}
      {/* <p> {JSON.stringify(message, null, 2)}</p> */}

      {/* <Connection /> */}
    </div>
  );
}}

export default App;
