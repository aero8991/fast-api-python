import React, { useEffect } from 'react'
import axios from "axios"
import { useState } from 'react'

const Connection = () => {
    const [result, setResult] = useState([])
    const [idCount, setIdCount] = useState(1)

       useEffect(() => {
         posts();
       }, []);
    const posts = async () => {
         try {
            const res = await axios.get("https://swapi.dev/api/people/2")
            console.log(res.data)
            setResult(res.data)
         }catch(err){
             console.log(err)}}
          



  return (
    <div>
    <div>Connection</div>
    {/* {result.map((data) => { 
        return <li key={data.name}>{data.name} {data.url}</li>
    })} */}
    <li>{result.name}</li>
    {console.log(result)}
    </div>
  )
}



export default Connection
