require 'winrm'
conn = WinRM::Connection.new(
  endpoint: 'http://localhost:5985/wsman',
  user: '<domain>\<user name>',
  password: '<password>',
)
command=""
conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        print "PS > "
        command = gets
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end
    puts "Exiting with code #{output.exitcode}"
end
