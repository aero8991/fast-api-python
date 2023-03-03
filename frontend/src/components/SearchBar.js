const SearchBar = ({ posts, setSearchResults, setSearch }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    const handleSearcher = () => {
      setSearch();
    };
  };

  const handleSearchChange = (e) => {
    // if (!e.target.value) return setSearchResults(posts);

    // const resultsArray = posts.filter(
    //   (post) =>
    //     post.title.includes(e.target.value) ||
    //     post.body.includes(e.target.value)
    // );

    // setSearchResults(resultsArray);

    setSearch(e.target.value)
  };

  return (
    <header>
      <form onSubmit={handleSubmit}>
        <input type="text" id="search" onChange={handleSearchChange} />

        <button>Click here!</button>
      </form>
    </header>
  );
};

export default SearchBar
