axios.post("url_to_request", json_data).then(
        async function (r) {
          console.log(r);
        }
      ).catch(
        function (e) {
          console.log(e)
        }
      )