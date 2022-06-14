# Use an another image as base for your Docker Image
# i.e: FROM postgres : You will create a Docker Image after the instuctions 
#                      installing PostreSQL.
FROM base-image

# Create an environment variable inside your Docker Container
# i.e: ENV HADOOP_PATH=/etc/hadoop : Once the container created, the environment variable
#                                    HADOOP_PATH will be available as is it for any
#                                    any environment variables from your Bash session
ENV my-env-variable=value

# Copy a file from the host into the container
# i.e: COPY ./my_script ./my_script : copy my_script located on the host at the current
#                                     directory of the Dockerfile into the container at 
#                                     the current directory which is / by default
COPY file_from_host to_container

# Execute a command inside the container
# i.e: RUN mkdir dir : create the directory /dir
RUN mkdir dir

# Indicate the port used by the container
# i.e: Airflow uses the port 8080 so we expose the port 8080
EXPOSE 8080

# Specify a command or script that will always be executed when the container starts
# i.e: ENTRYPOINT ["./entrypoint.sh"] : Execute the script entrypoint.sh located 
#                                       in the container
ENTRYPOINT [ "executable_that_will_be_always executed in first" ]

# Specify arguments that will be fed to the ENTRYPOINT if ENTRYPOINT exists otherwise
# run a command/script
# i.e: CMD ["ls"] : Execute the command ls inside the container
CMD [ "cmd to execute" ]
