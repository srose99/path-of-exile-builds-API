resource "aws_instance" "ec2-control" {
    ami = "ami-08766f81ab52792ce"
    instance_type = "t3.micro"
    subnet_id = aws_subnet.public_subnet.id
    vcp_security_group_ids = [aws_security_group.sg_custom.id]
    key_name = "poe_api_ec2_instance"

    tags = {
        "Name" "ec2-control"
    }
}

resource "aws_instance" "ec2-worker1" {
    ami = "ami-08766f81ab52792ce"
    instance_type = "t3.micro"
    subnet_id = aws_subnet.public_subnet.id
    vcp_security_group_ids = [aws_security_group.sg_custom.id]
    key_name = "poe_api_ec2_instance"

    tags = {
        "Name" "ec2-worker1"
    }
}

resource "aws_instance" "ec2-worker2" {
    ami = "ami-08766f81ab52792ce"
    instance_type = "t3.micro"
    subnet_id = aws_subnet.public_subnet.id
    vcp_security_group_ids = [aws_security_group.sg_custom.id]
    key_name = "poe_api_ec2_instance"

    tags = {
        "Name" "ec2-worker2"
    }
}