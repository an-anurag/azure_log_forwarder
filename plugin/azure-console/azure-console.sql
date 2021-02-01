
                
DELETE from plugin where id = 8902;
                
DELETE from plugin_sid where plugin_id = 8902;
                
INSERT ignore INTO plugin(id,type,name,description,vendor,product_type) values(8902,1,'Azure-Console','A Cloud Service','Microsoft',20);

INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, subcategory_id, class_id, priority, reliability, name) VALUES
                
(8902,1,1,1,NULL,2,2, 'Azure: Role assignments has been created by Admin'),
(8902,1,2,1,NULL,2,2, 'Azure: Virtual machine deleted by user'),
(8902,1,3,1,NULL,2,2, 'Azure: Virtual machine deallocated by user'),
(8902,1,4,1,NULL,2,2, 'Azure: Resource group created/updated by user'),
(8902,1,5,1,NULL,2,2, 'Azure: Generate SSH Key Pair'),
(8902,1,6,1,NULL,2,2, 'Azure: Deployment Validated by user'),
(8902,1,7,1,NULL,2,2, 'Azure: SSH Public Key Created or Updated by user'),
(8902,1,8,1,NULL,2,2, 'Azure: Virtual Machine Created or Updated by user'),
(8902,1,9,1,NULL,2,2, 'Azure: Virtual Machine started by user'),
(8902,1,10,1,NULL,2,2, 'Azure: Network security group created or updated'),
(8902,1,11,1,NULL,2,2, 'Azure: Public Ip Address for VM created or updated'),

(8902,10000,1,1,NULL,2,2, 'Azure: Generic administrative activity started'),
(8902,20000,1,1,NULL,2,2, 'Azure: Generic administrative activity succeeded');
