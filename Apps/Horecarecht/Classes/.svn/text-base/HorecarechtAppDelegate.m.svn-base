
//
//  HorecarechtAppDelegate.m
//  Horecarecht
//
//  Created by rabshakeh on 9/24/09 - 12:06 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "HorecarechtAppDelegate.h"
#import "HorecarechtViewController.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"

@implementation HorecarechtAppDelegate

@synthesize window;
@synthesize viewController;

-(void) applicationDidFinishLaunching: (UIApplication *) application
{
    TableViewFromDatabaseViewController *tableViewFromDatabaseController = [ [ TableViewFromDatabaseViewController alloc ] init ];
	
    tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk";
    tableViewFromDatabaseController.next_table = @"wetboek";
    tableViewFromDatabaseController.title      = @"Horecarecht - Apr.2011";
    [ tableViewFromDatabaseController reload ];
    navigationController = [ [ UINavigationController alloc ] initWithRootViewController:tableViewFromDatabaseController ];
	
    [ tableViewFromDatabaseController release ];
    navigationController.navigationBar.tintColor = [ UIColor colorWithRed:0.0 green:0.20392156862745098 blue:0.40000000000000002 alpha:0 ];
	
    [ window addSubview: [ navigationController view ] ];
	
    [ window makeKeyAndVisible ];
}


-(void) dealloc
{
    [ navigationController release ];
    [ viewController release ];
    [ window release ];
    [ super dealloc ];
}


@end
