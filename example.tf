module "my_ec2_instance {
    source = "https://github.com/onucheaboh/Endocode-Technical-Challenge"

    ec2_instance_type = "t3.micro"
    ec2_instance_name = "My instance"
    number_of_instances = 1
    ec2_ami_id = data.aws_ami.cloud_cobus.id 
}"