
                
DELETE from plugin where id = 8902;
                
DELETE from plugin_sid where plugin_id = 8902;
                
INSERT ignore INTO plugin(id,type,name,description,vendor,product_type) values(8902,1,'Azure-Console','A Cloud Service','Microsoft',20);

INSERT IGNORE INTO plugin_sid (plugin_id, sid, category_id, subcategory_id, class_id, priority, reliability, name) VALUES
                
(8902,1,1,1,NULL,2,2, 'Azure: -------------------'),


(8902,10000,1,1,NULL,2,2, 'Azure: Root User generic activity event'),
(8902,20000,1,1,NULL,2,2, 'Azure: IAM user generic activity event');
