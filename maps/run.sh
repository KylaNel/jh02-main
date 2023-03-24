# |Please keep with file on LF not CRLF
echo "run.sh: Copying style file into /data volume"
mv -f "style.json" "/data"
echo "run.sh: Copying mbtiles into /data volume"
mv -f "map.mbtiles" "/data"
echo "run.sh: Copying config into /data volume"
mv -f "config.json" "/data"
echo "run.sh: Running the maputnik --watch command on style file"
/maputnik --watch --file "/data/style.json"