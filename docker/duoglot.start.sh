echo "GITSTATUS" > $PWD/__gitstatus
git rev-parse HEAD >> $PWD/__gitstatus
git status | grep "working tree clean" >> /tmp/__gitstatus

if [[ -z "${WORKSPACEROOT}" ]]; then
  docker compose -f duoglot.docker-compose.yml up
else
  PWD=$WORKSPACEROOT/docker docker compose -f duoglot.docker-compose.yml up
fi